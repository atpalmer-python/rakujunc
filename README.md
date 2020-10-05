# Python "Raku Junctions" (rakujunc)

An implementation in Python of the "Junctions" concept from the Raku language (previously called Perl 6).

Raku Junction docs:

https://docs.raku.org/type/Junction


## Examples

```
    import rakujunc as junc

    assert junc.one(*range(1, 31)) == 3     # Passes
    assert junc.any('a', 'b', 'c') == 'a'   # Passes

    if junc.any(1, 2) + 1 == 3:
        print('yes')  # prints 'yes'
```
