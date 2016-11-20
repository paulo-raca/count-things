# Count things
Did you ever want a dead-simple service to assign build numbers, serial numbers, etc? This is it.

## Counter Identifiers
This service hosts many different counters -- How many builds have been made of v1.9.35 of libfoo, serial numbers of Device Foo, etc.

To distinguish between those, each counter has an hierarchical Identifier, identified by it's path. for instance, `mycompany.com/libfoo/v1.9.35/build/` and `foodevices.com/foodevice/serial_number/`.

Keep in mind that:
- To avoid conflicts, the first element of the identifier should your domain name. For testing purposes, you should use `example.com`.
- Counter identifiers always end with a trailling slash

## Item identifier
You can link an unique identifier to each value of the counter.

For example, you can link your build number with the git commit hash, and your device serial number with it's MAC Address.

If you use an identifier, the counter will be incremented the first time you access it, but the same value is always going to be returned afterwards.
