# data-development-donations
A space for developing data for Feminist AI LAN Partys


## LLMs

Text-generation and notebooks for text generation.

## Diffusion

Image and diffustion model outputs/data and notebooks/ideas.


## Prodigy database

File `prodigy.json` in the current working directory

```json
{
  "db": "postgresql",
  "db_settings": {
    "postgresql": {
      "host": "192.168.88.10",
      "port": 5432,
      "dbname": "femai",
      "user": "prodigy",
      "password": "prodigyrocks"
    }
  }
}
```

Install database driver:

```bash
pip install psycopg2 --no-binary
```

Test that it works:

```bash
python -m prodigy stats
```

## How to contribute

Fork the repo, do a PR from fork.