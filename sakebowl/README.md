# Sakebowl
## Docker
### Variables
- `PRODUCTION`: any value but "" (empty string) runs Sakebowl in production mode
- `SECRET_KEY`: secret key used for Django
- `STATIC`: Djangos static directory, defaults to `./static`
- `DB`: Path for Djangos SQLite DB (this should point to a mount or bind)