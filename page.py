import panel as pn
import holoviews as hv

pn.extension()

def page():
    p = pn.template.VanillaTemplate(header=[pn.pane.Str("Hello")])
    p.main.append(
        pn.Row(
            pn.Card(pn.pane.Str("A card containing some text")),
            pn.Card(hv.Curve([1, 2, 3])),
        )
    )
    return p
