class Base:

    def test(self) -> None:
        print('test')


class Foo(Base):
    name = 'Foo'

    def action(self) -> None:
        print(self.name)


class Bar(Foo):
    name = 'Bar'
