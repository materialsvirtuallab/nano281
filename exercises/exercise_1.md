# Exercise 1 - Python for Data Science

This short exercise is meant to provide a quick guide to various features in the Python programming language and the
Scientific Python packages. It is highly recommended that all students attempt this exercise prior to the solutions
being posted.

1. Write a Python method using only the standard library - no external packages or methods - to compute the distance 
   between the points (x1, y1) and (x2, y2). Make sure you test it out properly.
2. Do the same thing as (1) but using built-in numpy methods.
3. Write a Python class (please refer to [Python documentation](https://docs.python.org/3/tutorial/classes.html) to
   find out what a class is and how to make one) to represent an n-sided regular polygon with vertices at a distance r
   from the center. Note that n and r should be inputs to your class. E.g., a square of with diagonals of length 2 can
   be instantiated as `Polygon(4, 1)`.
4. Add a method called get_vertices to your Polygon class, which will return a Python list of coordinates (xi, yi) for
   the vertices. This is not uniquely defined of course, but you can choose any scheme that results in a regular polygon.
   Hint: think of how to get the angles of polygon and construct the points from there.
5. Add a method called get_perimeter to your Polygon class, which will compute the perimeter of the Polygon based on
   the vertices obtained in (4) and the distance code in qn (1)/(2).
6. Using your class in 4, construct a Python Data Frame with n = 3-100 (inclusive) with r = 1 with the following
   columns: n, r, perimeter.
7. In your DataFrame in 6, add a column for the percentage difference between the perimeter of the n-side Polygon and a
   circle of radius 1.
8. Using matplotlib or seaborn or any other means, plot the relationship between the percentage difference between the
   perimeter of the n-side Polygon and a circle of radius 1 against n. Label your x and y axes properly.