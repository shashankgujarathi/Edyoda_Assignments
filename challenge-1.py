class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def sqSum(self):
        x_sq = self.x**2
        y_sq = self.y**2
        z_sq = self.z**2
        return x_sq + y_sq + z_sq

point_obj = Point(1,3,5)
print(point_obj.sqSum())