import setuptools

setuptools.setup(
   name="jupyter-openservers",
   description="Jupyter Server Proxy for Streamlit/VScode/Dagster",
   version="0.0.1",
   author="Patrick Sipple",
   py_modules=["openservers"],
   entry_points={
       "jupyter_serverproxy_servers": [
           # name = packagename:function_name
           "Streamlit = openservers:setup_openstreamlit",
           "VSCode = openservers:setup_openvscode",
           "Dagster = openservers:setup_opendagster",
       ]
   },
   install_requires=["jupyter-server-proxy", "streamlit", "dagster", "dagster-webserver"],
   data_files=[("icons", ["icons/streamlit.svg", "icons/vscode.svg", "icons/dagster.svg", "icons/index.html"])],
)
