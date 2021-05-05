import Pyro5.api as p5

ns = p5.locate_ns()
uri = ns.lookup('obj')

#o = Pyro4.Proxy('PYRO:obj_6bc3296b2d8745828247253eb0a654e1@localhost:54218')
o = p5.Proxy(uri)

print(o.listarPerfil('kellypinto@yahoo.com'))