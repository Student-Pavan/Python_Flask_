# Flask Basic Concepts

## Overview
This is a basic Flask web application demonstrating core Flask concepts and functionality. The project was initially an empty repository and has been set up as a complete, working Flask application on Replit.

**Created:** October 16, 2025  
**Status:** Fully functional and ready to use

## Project Purpose
This application serves as an educational resource for learning Flask basics, including:
- Routing and URL mapping
- Template rendering with Jinja2
- Static file serving
- RESTful API development
- Flask application structure

## Recent Changes
- **October 16, 2025**: Complete initial setup
  - Created Flask application structure with `app.py`
  - Added HTML templates with base template inheritance
  - Implemented multiple routes (/, /about, /api/hello)
  - Added CSS styling for responsive design
  - Configured development and production environments
  - Set up Gunicorn for production deployment

## Project Architecture

### File Structure
```
.
├── app.py                 # Main Flask application
├── templates/             # HTML templates
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   └── about.html        # About page
├── static/               # Static assets
│   └── css/
│       └── style.css     # Application styles
├── .pythonlibs/          # Python virtual environment (auto-generated)
├── .replit               # Replit configuration
└── replit.md             # This file
```

### Key Components

#### Application (app.py)
- Flask app initialization
- Route definitions for three endpoints:
  - `/` - Home page with feature overview
  - `/about` - About page with Flask concepts
  - `/api/hello` - JSON API endpoint
- Development server configured on `0.0.0.0:5000`

#### Templates
- **base.html**: Base template with navigation and layout structure
- **index.html**: Home page extending base template with interactive API test
- **about.html**: Educational content about Flask concepts

#### Static Files
- Responsive CSS with gradient background
- Modern, clean UI design
- Mobile-friendly layout

## Technology Stack
- **Python**: 3.11
- **Framework**: Flask 3.1.2
- **Template Engine**: Jinja2 3.1.6
- **Production Server**: Gunicorn 23.0.0
- **Package Manager**: UV (Replit's Python package manager)

## Development

### Running Locally
The Flask development server runs automatically via the configured workflow:
```bash
python app.py
```
Access at: http://localhost:5000

### API Endpoints
- `GET /` - Home page
- `GET /about` - About page  
- `GET /api/hello` - Returns JSON: `{"message": "Hello from Flask API!", "status": "success"}`

### Features Demonstrated
1. **Routing**: Multiple URL endpoints with Flask decorators
2. **Templates**: Jinja2 template inheritance and rendering
3. **Static Files**: CSS serving through Flask's static folder
4. **API Development**: JSON response endpoint
5. **Development Server**: Debug mode with auto-reload

## Deployment
The application is configured for Replit's autoscale deployment using Gunicorn:
```bash
gunicorn --bind=0.0.0.0:5000 --reuse-port app:app
```

Deployment type: **autoscale** (stateless web application)

## Environment Configuration
- **Development**: Flask development server with debug mode
- **Production**: Gunicorn WSGI server with port reuse
- **Host**: 0.0.0.0 (allows Replit proxy access)
- **Port**: 5000 (required for Replit frontend)

## User Preferences
None specified yet.

## Notes
- The application is configured to work with Replit's proxy/iframe architecture
- Debug mode is enabled in development for easier debugging
- Cache-Control headers may need to be added if caching issues occur
- The 404 error for favicon.ico in browser logs is normal and can be ignored
