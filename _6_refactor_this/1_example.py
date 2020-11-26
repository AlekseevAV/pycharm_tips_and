class Base:

    def test(self):
        print('test')


class Foo(Base):
    name = 'Foo'

    def action(self):
        print(self.name)

    def test(self):
        a = 5
        c = a * 2
        super().test()


class Bar(Foo):
    name = 'some_name'

    def __str__(self) -> str:
        return super().__str__()

    def action(self):
        super().action()

    def test(self):
        super().test()
