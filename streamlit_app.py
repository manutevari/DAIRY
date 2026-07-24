"""Streamlit entrypoint for the DairyTwinOS enterprise architecture."""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).parent
ARCHITECTURE_DOC = ROOT / "docs" / "architecture.md"


@st.cache_data
def load_architecture_markdown() -> str:
    """Load the architecture document from disk."""
    return ARCHITECTURE_DOC.read_text(encoding="utf-8")


def extract_mermaid(markdown: str) -> str:
    """Extract the first Mermaid code block from a Markdown document."""
    fence = "```mermaid"
    start = markdown.find(fence)
    if start == -1:
        return ""

    content_start = start + len(fence)
    end = markdown.find("```", content_start)
    if end == -1:
        return ""

    return markdown[content_start:end].strip()


def render_mermaid(diagram: str) -> None:
    """Render a Mermaid diagram inside Streamlit."""
    components.html(
        f"""
        <div class="mermaid">
        {diagram}
        </div>
        <script type="module">
          import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";

          mermaid.initialize({{
            startOnLoad: true,
            theme: "base",
            securityLevel: "strict",
            themeVariables: {{
              primaryColor: "#e7f6f3",
              primaryTextColor: "#102033",
              primaryBorderColor: "#137c6d",
              lineColor: "#6d7d8f",
              secondaryColor: "#f3f7fb",
              tertiaryColor: "#ffffff",
              fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
            }}
          }});
        </script>
        """,
        height=4200,
        scrolling=True,
    )


st.set_page_config(
    page_title="DairyTwinOS Enterprise Architecture",
    page_icon="🥛",
    layout="wide",
)

st.title("🥛 DairyTwinOS Enterprise Architecture")
st.caption("Streamlit deployment target for the DairyTwinOS master architecture roadmap.")

st.markdown(
    """
    Explore the full DairyTwinOS roadmap from foundation through ultimate enterprise,
    including frontend experiences, Streamlit workflows, FastAPI services, plant equipment,
    SCADA, MES, AI, deployment, and production packaging.
    """
)

architecture_markdown = load_architecture_markdown()
mermaid_diagram = extract_mermaid(architecture_markdown)

if not mermaid_diagram:
    st.error("No Mermaid architecture diagram was found in docs/architecture.md.")
else:
    tab_diagram, tab_source = st.tabs(["Rendered diagram", "Markdown source"])

    with tab_diagram:
        render_mermaid(mermaid_diagram)

    with tab_source:
        st.markdown(architecture_markdown)
