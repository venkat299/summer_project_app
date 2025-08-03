# import unittest
# from unittest.mock import patch
# from main import crew

# class TestCrew(unittest.TestCase):

#     @patch('crewai.Crew.kickoff')
#     def test_crew_kickoff(self, mock_kickoff):
#         # Arrange
#         expected_result = {
#             "skills": [
#               {"skill": "Python", "weight": 5},
#               {"skill": "Django/Flask/FastAPI", "weight": 4},
#               {"skill": "Object-Oriented Programming", "weight": 4},
#               {"skill": "ORM Libraries", "weight": 3},
#               {"skill": "Database Schema Design", "weight": 4},
#               {"skill": "Git", "weight": 3}
#             ],
#             "experience": {
#               "years": 5,
#               "weight": 5
#             },
#             "responsibilities": [
#               {"responsibility": "Design, build, and maintain Python code", "weight": 5},
#               {"responsibility": "Integrate user-facing elements", "weight": 4},
#               {"responsibility": "Solve complex performance problems", "weight": 4},
#               {"responsibility": "Integrate data storage solutions", "weight": 2}
#             ]
#           }
#         mock_kickoff.return_value = expected_result

#         # Act
#         result = crew.kickoff()

#         # Assert
#         self.assertEqual(result, expected_result)
#         mock_kickoff.assert_called_once()

# if __name__ == '__main__':
#     unittest.main()
