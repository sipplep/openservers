from setuptools import find_packages, setup

setup_args = dict(
   name="jupyter-openservers",
   description="Jupyter Server Proxy for Streamlit/VScode",
   version="0.0.1",
   author="Patrick Sipple",
   packages=find_packages(),
   entry_points={
       "jupyter_serverproxy_servers": [
           # name = packagename:function_name
           "Streamlit = openservers:setup_openstreamlit",
           "Code = openservers:setup_openvscode",
           "Dagster = openservers:setup_opendagster",
       ]
   },
   install_requires=["jupyter-server-proxy", "streamlit", "dagster-webserver"],
    package_data={
        "openservers": ["icons/*"],
    },
)

if __name__ == "__main__":
    setup(**setup_args)