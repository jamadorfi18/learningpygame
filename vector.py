# This file is part of learningpygame
#
# learningpygame is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# learnigpygame is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pygame.  If not, see <http://www.gnu.org/licenses/>.


class Vector(object):
    """
    Represent a vector of movement
    """

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    @staticmethod
    def create_from_points(p1, p2):
        return Vector(p2[0]-p1[0], p2[1] - p1[1])
