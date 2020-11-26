class Base:

    def test(self):
        print('test')


class Foo(Base):
    name = 'Foo'

    def action(self):
        print(self.name)


class Bar(Foo):
    name = 'Bar'

    def __str__(self) -> str:
        return super().__str__()

    def action(self):
        super().action()

    def test(self):
        super().test()


