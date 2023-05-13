import unittest
from prototype import *


class SomeComponentTest(unittest.TestCase):

    def test_shallow_copy(self):
        list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
        circular_ref = SelfReferencingEntity()
        component = SomeComponent(23, list_of_objects, circular_ref)
        circular_ref.set_parent(component)

        shallow_copied_component = copy.copy(component)

        # Verify that the shallow copied object is not the same as the original object
        self.assertIsNot(component, shallow_copied_component)

        # Verify that the shallow copied object's attributes are the same as the original object's attributes
        self.assertEqual(component.some_int, shallow_copied_component.some_int)
        self.assertEqual(component.some_list_of_objects, shallow_copied_component.some_list_of_objects)
        self.assertEqual(component.some_circular_ref, shallow_copied_component.some_circular_ref)

        # Verify that changing attributes in the shallow copied object does not affect the original object
        shallow_copied_component.some_int = 42
        self.assertNotEqual(component.some_int, shallow_copied_component.some_int)

    def test_deep_copy(self):
        list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
        circular_ref = SelfReferencingEntity()
        component = SomeComponent(23, list_of_objects, circular_ref)
        circular_ref.set_parent(component)

        deep_copied_component = copy.deepcopy(component)

        # Verify that the deep copied object is not the same as the original object
        self.assertIsNot(component, deep_copied_component)

        # Verify that the deep copied object's attributes are the same as the original object's attributes
        self.assertEqual(component.some_int, deep_copied_component.some_int)
        self.assertEqual(component.some_list_of_objects, deep_copied_component.some_list_of_objects)
        self.assertEqual(component.some_circular_ref, deep_copied_component.some_circular_ref)

        # Verify that changing attributes in the deep copied object does not affect the original object
        deep_copied_component.some_int = 42
        self.assertNotEqual(component.some_int, deep_copied_component.some_int)

        # Verify that changing attributes in the deep copied object's nested objects does not affect the original object
        deep_copied_component.some_list_of_objects.append("another object")
        self.assertNotIn("another object", component.some_list_of_objects)
        deep_copied_component.some_list_of_objects[1].add(4)
        self.assertNotIn(4, component.some_list_of_objects[1])

    def test_circular_reference(self):
        list_of_objects = [1, {1, 2, 3}, [1, 2, 3]]
        circular_ref = SelfReferencingEntity()
        component = SomeComponent(23, list_of_objects, circular_ref)
        circular_ref.set_parent(component)

        deep_copied_component = copy.deepcopy(component)

        # Verify that the circular reference is maintained in the deep copied object
        self.assertEqual(deep_copied_component.some_circular_ref.parent, deep_copied_component)
        self.assertEqual(deep_copied_component.some_circular_ref.parent.some_circular_ref.parent, deep_copied_component.some_circular_ref)

        # Verify that the circular reference is not the same as the original object's circular reference
        self.assertIsNot(component.some_circular_ref, deep_copied_component.some_circular_ref)
        self.assertIsNot(component.some_circular_ref.parent,
