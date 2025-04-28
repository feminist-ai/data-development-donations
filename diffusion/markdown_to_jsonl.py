import json
import argparse

def markdown_to_jsonl(markdown_text):
    """Convert a markdown table to JSONL, extracting image filenames from the image column."""
    # Split into lines and remove empty lines
    lines = [line for line in markdown_text.strip().split('\n') if line.strip()]
    
    if len(lines) < 3:  # Need at least header, separator, and one data row
        return ""
    
    # Extract headers
    headers = [h.strip() for h in lines[0].strip().split('|')[1:-1]]
    
    # Process data rows
    jsonl_output = []
    for i in range(2, len(lines)):
        row_values = [cell.strip() for cell in lines[i].strip().split('|')[1:-1]]
        
        row_object = {}
        for j, header in enumerate(headers):
            if j < len(row_values):
                value = row_values[j].replace("<br>", "\n")
                
                # Special handling for 'output' column with markdown image links
                if header == 'image' and value.startswith('![') and ')' in value:
                    # Extract just the filename from the markdown image link ![](filename)
                    value = value.split('](')[1].split(')')[0]
                
                row_object[header] = value
            else:
                row_object[header] = ""
        
        jsonl_output.append(json.dumps(row_object))
    
    return "\n".join(jsonl_output)


def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Convert markdown table to JSONL with special handling for image links')
    parser.add_argument('input_file', help='Input file containing markdown table')
    parser.add_argument('output_file', help='Output file to write JSONL data')
    
    args = parser.parse_args()
    
    try:
        # Read input file
        with open(args.input_file, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        
        # Convert markdown to JSONL
        jsonl_content = markdown_to_jsonl(markdown_content)
        
        # Write output file
        with open(args.output_file, 'w', encoding='utf-8') as file:
            file.write(jsonl_content)
            
        print(f"Successfully converted {args.input_file} to {args.output_file}")
        
    except FileNotFoundError:
        print(f"Error: Could not find input file {args.input_file}")
    except PermissionError:
        print(f"Error: Permission denied when accessing file")
    except Exception as e:
        print(f"Error during conversion: {str(e)}")


if __name__ == "__main__":
    main()