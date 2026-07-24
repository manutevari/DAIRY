# DairyTwinOS

DairyTwinOS is an enterprise roadmap and reference architecture for a dairy plant digital twin platform.

- [Enterprise master architecture](docs/architecture.md)

## Deployment

### Vercel

This repository includes `index.html` and `vercel.json`, so it can be deployed to Vercel as a static site with no build command.

### Streamlit

This repository also includes `streamlit_app.py`, `requirements.txt`, and `.streamlit/config.toml`, so it can be deployed on Streamlit Community Cloud. Set the app entrypoint to `streamlit_app.py`.

To run locally:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
