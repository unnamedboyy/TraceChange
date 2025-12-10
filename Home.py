import streamlit as st

# Page Configuration -------------------------------------------------
st.set_page_config(
    page_title="Table Compare Tool",
    page_icon="📊",
    layout="wide"
)

# Hero Section -------------------------------------------------
st.title("📊 Table Compare Tool")
st.markdown(
    """
Welcome to **Table Compare Tool**, a Streamlit-based application designed to identify 
differences between two tabular datasets.  
This interface serves as the main entry point to the platform.
"""
)

# Application Overview -------------------------------------------------
with st.container(border=True):
    st.subheader("What This Application Does")
    st.markdown(
        """
This tool allows you to compare two dataset versions (*Old* and *New*) and provides 
a clear breakdown of how rows have changed. It supports:

- **Added** rows  
- **Deleted** rows  
- **Modified** rows  
- **Duplicate** rows  
- **Same** rows  

Additional features include:

- Automatic column change detection  
- Excel export with color-coded highlighting  
- Interactive preview with row filtering  
- Duplicate row merging  
        """
    )

# Workflow Explanation -------------------------------------------------
with st.expander("🔄 How the Comparison Workflow Operates", expanded=False):
    st.markdown(
        """
### 1. Upload Your Files  
Upload one *Old* dataset and one *New* dataset (CSV or Excel).

### 2. Select a Key Column  
Choose a column that exists in both files to be used as the comparison key  
(case-insensitive matching when possible).

### 3. Run the Comparison  
The tool aligns rows and identifies:
- Added (exist only in the new file)  
- Deleted (exist only in the old file)  
- Modified (same key, different values)  
- Duplicate (repeated rows)  

### 4. Review the Results  
Use the status tabs to navigate differences:
- All  
- Added  
- Modified  
- Deleted  
- Duplicate  

Each section allows you to select which rows should be included in the final output.

### 5. Export  
Download your results as:  
- **Plain Excel**  
- **Colored Excel** (highlighted changes)
        """
    )

# Developer Information -------------------------------------------------
with st.container(border=True):
    st.subheader("About the Developer")
    st.markdown(
        """
This application was developed by **Kaisar Simatupang**  
as a practical solution for dataset comparison workflows.

**Technology Stack Used**
- Python  
- Streamlit  
- Pandas  
- OpenPyXL  
        """
    )

st.markdown("---")
st.info("Use the sidebar to access the comparison module and begin analyzing your data.")
