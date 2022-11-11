# Making a Jupyter Server Release

## Using `jupyter_releaser`

The recommended way to make a release is to use [`jupyter_releaser`](https://jupyter-releaser.readthedocs.io/en/latest/get_started/making_release_from_repo.html).

## Manual Release

To create a manual release, perform the following steps:

### Set up

```bash
pip install pipx
git pull origin $(git branch --show-current)
git clean -dffx
```

### Update the version and apply the tag

```bash
echo "Enter new version"
read script_version
pipx run hatch version ${script_version}
git tag -a ${script_version} -m "${script_version}"
```

### Build the artifacts

```bash
rm -rf dist
pipx run build .
```

### Update the version back to dev

```bash
echo "Enter dev version"
read dev_version
pipx run hatch version ${dev_version}
git push origin $(git branch --show-current)
```

### Publish the artifacts to pypi

```bash
pipx run twine check dist/*
pipx run twine upload dist/*
```
