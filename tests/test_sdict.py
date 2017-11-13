import unittest

import pickle

from sdict import sdictm, sdict

__author__ = 'anand'

d = dict(a=1, b=2, c=dict(d=3, g=1, e=dict(f=4)))


class TestSdict(unittest.TestCase):
    def test_different_forms_of_assignment(self):
        # TEST DIFFERENT FORMS OF ASSIGNMENT
        sd = sdictm(d)

        sd.a = 13
        sd['b'] = 14

        sd.c['d'] = 51
        sd['c']['g'] = 52
        sd.c.e.f = 10

        self.assertEqual(sd.todict(), dict(a=13, b=14, c=dict(d=51, g=52, e=dict(f=10))))
        self.assertEqual(pickle.loads(pickle.dumps(sd)).todict(), sd.todict())

    def test_assignment_after_getattr(self):
        # TEST ASSIGNMENT AFTER GETATTR
        sd1 = sdictm(d)

        sdc = sd1.c
        sdc.d = 15

        self.assertEqual(sd1.todict(), dict(a=1, b=2, c=dict(d=15, g=1, e=dict(f=4))))

    def test_sdict_is_immutable(self):
        # TEST THAT SDICT IS INDEED IMMUTABLE (ALSO ACCESS OF VARIOUS ATTRIBUTES)
        sd2 = sdict(d)
        # print(sd2.a, sd2.c.d, sd2.c.e.f)
        with self.assertRaises(NotImplementedError):
            sd2.a = 100
        with self.assertRaises(NotImplementedError):
            sd2['b'] = 100
        with self.assertRaises(NotImplementedError):
            sd2.c['d'] = 100
        with self.assertRaises(NotImplementedError):
            sd2['c']['g'] = 100
        with self.assertRaises(NotImplementedError):
            sd2.c.e.f = 100

        self.assertEqual(sd2.todict(), d)

    def test_copy(self):
        # TEST THAT THE COPY DOES COPY VALUES
        sd2 = sdict(d)
        sd3 = sd2.copy()
        self.assertNotEqual(id(sd2), id(sd3))
        self.assertEqual(sd3.a, sd2.a)
        self.assertEqual(sd3.c.d, sd2.c.d)
        self.assertEqual(sd3.c.e.f, sd2.c.e.f)
        # print(sd3.a, sd3.c.d, sd3.c.e.f)

    def test_creation_of_new_variable(self):
        # TEST THAT CREATION OF NEW VARIABLE WORKS
        sd4 = sdictm(d)

        sd4.c.h = 10

        self.assertEqual(sd4.todict(), dict(a=1, b=2, c=dict(d=3, g=1, h=10, e=dict(f=4))))

    def test_copy_2(self):
        # TEST THAT COPY CREATES A NEW INSTANCE ENITRELY
        sd5 = sdictm(d)
        sd6 = sd5.copy()
        sd6.c.d = 123
        self.assertEqual(sd6.todict(), dict(a=1, b=2, c=dict(d=123, g=1, e=dict(f=4))))
        self.assertEqual(sd5.todict(), d, sd5.todict())

    def test_update(self):
        # TEST WITH UPDATES
        sd7 = sdictm(d)
        sd8 = sd7.update(a=10).copy()
        sd9 = sd7.update(a=1, d=5).copy()
        self.assertEqual(sd8.todict(), dict(a=10, b=2, c=dict(d=3, g=1, e=dict(f=4))))
        self.assertEqual(sd9.todict(), dict(a=1, b=2, d=5, c=dict(d=3, g=1, e=dict(f=4))))

    def test_frozen(self):
        # TEST FROZEN
        sd11 = sdictm(d)
        sd12 = sd11.frozen()

        with self.assertRaises(NotImplementedError):
            sd12.a = 100
        with self.assertRaises(NotImplementedError):
            sd12['b'] = 100
        with self.assertRaises(NotImplementedError):
            sd12.c['d'] = 100
        with self.assertRaises(NotImplementedError):
            sd12['c']['g'] = 100
        with self.assertRaises(NotImplementedError):
            sd12.c.e.f = 100

        self.assertEqual(sd12.todict(), d)

    def test_list_in_dict(self):
        # TEST LIST IN DICTIONARY
        dd = dict(a=[1, 2, 3], b=[dict(one=1, two=2), dict(three=3)], c=dict(d=3, g=1, e=dict(f=4)))
        sd13 = sdictm(dd)
        self.assertEqual(sd13.todict(), dd)

    def test_nested_assignment_dot(self):
        # TEST that nested assignment works with dot notation
        sd = sdictm(dict(a=13))
        sd.x.y = 20
        self.assertEqual(sd.todict(), dict(a=13, x=dict(y=20)))

    def test_nested_assignment_string(self):
        # TEST that nested assignment works with string
        sd = sdictm(dict(a=13))
        sd['x.y'] = 20
        self.assertEqual(sd.todict(), dict(a=13, x=dict(y=20)))

    def test_nested_retrieve_string(self):
        # TEST that nested retrieve works with string
        sd = sdictm(dict(a=dict(b=dict(c=13))))
        self.assertEqual(sd['a.b.c'], 13)

    def test_immutable_doesnt_change_after_access_of_unknown_attr(self):
        dd = dict(a=dict(b=dict(c=13)))
        sd = sdict(dd)
        a = sd.x
        self.assertIsNone(a)
        self.assertEqual(sd.todict(), dd)


if __name__ == '__main__':
    unittest.main()
