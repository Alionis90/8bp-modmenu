# Plugin contract

Every modmenu feature lives in `plugins/<name>/plugin.py` and exports a
`PLUGIN` symbol pointing to a subclass of `src.shared.contracts.ModPlugin`.

```python
class MyFeature(ModPlugin):
    name = "my_feature"
    version = "0.1.0"

    def on_load(self) -> None: ...
    def on_tick(self, payload) -> None: ...

PLUGIN = MyFeature
```

The host calls `on_load` once and `on_tick` every frame. Publish to
`self.ctx.bus` with topics prefixed by `overlay:` to draw, or use
`skin:` to swap skins.