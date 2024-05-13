import setuptools

setuptools.setup(
   name="jupyter-openservers",
   description="Jupyter Server Proxy for Streamlit/VScode",
   version="0.0.1",
   author="Patrick Sipple",
   py_modules=["openservers"],
   entry_points={
       "jupyter_serverproxy_servers": [
           # name = packagename:function_name
           "Streamlit = openservers:setup_openstreamlit",
           "VS Code = openservers:setup_openvscode",
           "Dagster Dev = openservers:setup_opendagster",
       ]
   },
   install_requires=["jupyter-server-proxy", "streamlit", "dagster-webserver"],
)
