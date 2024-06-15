Commands to test:

```
rm -rf ~/rpmbuild
rpmdev-setuptree
cp *.spec ~/rpmbuild/SPECS/
cp *.tar.xz ~/rpmbuild/SOURCES/
```

```
rpmbuild -bb ~/rpmbuild/SPECS/
```
