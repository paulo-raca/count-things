# Count things
Did you ever want a dead-simple service to assign build numbers, serial numbers, etc? This is it.

## Counter Identifiers
This service hosts many different counters -- How many builds have been made of v1.9.33 of libfoo, serial numbers of Device Foo, etc.

To distinguish between those, each counter has an hierarchical Identifier, identified by it's path. for instance, `mycompany.com/libfoo/v1.9.35/build/` and `foodevices.com/foodevice/serial_number/`.

Keep in mind that:
- To avoid conflicts, the first element of the identifier should your domain name.

  For testing purposes, you should use `example.com`.
- Counter identifiers always end with a trailling slash

To start counting, just access it's URL: 

For example, on libfoo:
```
$ curl https://count-things.appspot.com/example.com/libfoo/v1.9.33/build/
1
$ curl https://count-things.appspot.com/example.com/libfoo/v1.9.33/build/
2
$ curl https://count-things.appspot.com/example.com/libfoo/v1.9.33/build
3
```

For example, on Foo Device:
```
$ curl https://count-things.appspot.com/example.com/foodevice/serial_number/
1
$ curl https://count-things.appspot.com/example.com/foodevice/serial_number/
2
$ curl https://count-things.appspot.com/example.com/foodevice/serial_number/
3
```

## Item identifier
You can link an unique identifier to each value of the counter.

For example, you can link your build number with the git commit hash, and your device serial number with it's MAC Address.

If you use an identifier, the counter will be incremented the first time you access it, but the same value is always going to be returned afterwards.

To use an identifier, just append it to the counter identifier

For example, on libfoo:
```
$ curl https://count-things.appspot.com/example.com/libfoo/v1.9.33/build/697ed8d03909140d95484d46d277a4e46d89b0e5
4
$ curl https://count-things.appspot.com/example.com/libfoo/v1.9.33/build/697ed8d03909140d95484d46d277a4e46d89b0e5
4
$ curl https://count-things.appspot.com/example.com/libfoo/v1.9.33/build/0f0909e242f73c1154272cf04f07fc9afe13e5b8
5
$ curl https://count-things.appspot.com/example.com/libfoo/v1.9.33/build/0f0909e242f73c1154272cf04f07fc9afe13e5b8
5
$ curl https://count-things.appspot.com/example.com/libfoo/v1.9.33/build/697ed8d03909140d95484d46d277a4e46d89b0e5
4
```

For example, on Foo Device:
```
$ curl https://count-things.appspot.com/example.com/foodevice/serial_number/ee:9e:bd:a7:61:69
4
$ curl https://count-things.appspot.com/example.com/foodevice/serial_number/ee:9e:bd:a7:61:69
4
curl https://count-things.appspot.com/example.com/foodevice/serial_number/02:42:68:5d:68:4d 
5
$curl https://count-things.appspot.com/example.com/foodevice/serial_number/ee:9e:bd:a7:61:69
4
```
