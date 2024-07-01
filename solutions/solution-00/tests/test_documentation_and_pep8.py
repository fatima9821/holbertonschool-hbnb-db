""" This script checks if all modules, classes, functions, and methods have docstrings."""

import os
import unittest
import ast
import pycodestyle


class TestDocumentation(unittest.TestCase):
    """Tests to ensure docstring compliance and PEP8."""

    def test_documentation(self):
        """Check if all modules, classes, functions, and methods have docstrings."""
        root_dir = os.path.abspath("./src")  # specify your root directory here
        for root, _, files in os.walk(root_dir):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "r", encoding="utf-8") as f:
                        file_content = f.read()
                    tree = ast.parse(file_content, filename=file_path)
                    self.check_docstrings(tree, file_path)

    def check_docstrings(self, node, file_path):
        """Recursively check docstrings in AST nodes."""
        if isinstance(node, ast.Module):
            self.assertIsNotNone(
                ast.get_docstring(node), f"Module {file_path} is missing a docstring"
            )

        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                self.assertIsNotNone(
                    ast.get_docstring(child),
                    f"Function {child.name} in {file_path} is missing a docstring",
                )
            elif isinstance(child, ast.ClassDef):
                self.assertIsNotNone(
                    ast.get_docstring(child),
                    f"Class {child.name} in {file_path} is missing a docstring",
                )
                for class_child in child.body:
                    if isinstance(class_child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        self.assertIsNotNone(
                            ast.get_docstring(class_child),
                            f"Method {class_child.name} in class {child.name} in {file_path} is missing a docstring",
                        )
            self.check_docstrings(child, file_path)

    def test_pep8_compliance(self):
        """Check PEP8 compliance using pycodestyle."""
        root_dir = os.path.abspath("./src")
        style_guide = pycodestyle.StyleGuide()
        report = style_guide.check_files([root_dir])
        self.assertEqual(
            report.total_errors,
            0,
            f"Found PEP8 errors and warnings: {report.total_errors}",
        )


if __name__ == "__main__":
    unittest.main()
