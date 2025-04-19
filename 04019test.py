import requests
import unittest

class TestPostRequests(unittest.TestCase):
    def test_post_request_1(self):
        """
        测试用例1：发送POST请求到指定URL
        """
        url = "https://jsonplaceholder.typicode.com/posts"
        data = {
            "title": "Test Post",
            "body": "This is a test post request",
            "userId": 1
        }
        
        response = requests.post(url, json=data)
        
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())
        self.assertEqual(response.json()["title"], "Test Post")
        self.assertEqual(response.json()["body"], "This is a test post request")
        self.assertEqual(response.json()["userId"], 1)

    def test_post_request_2(self):
        """
        测试用例2：发送POST请求到另一个URL
        """
        url = "https://jsonplaceholder.typicode.com/comments"
        data = {
            "postId": 1,
            "name": "Test Comment",
            "email": "test@example.com",
            "body": "This is a test comment"
        }
        
        response = requests.post(url, json=data)
        
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())
        self.assertEqual(response.json()["postId"], 1)
        self.assertEqual(response.json()["name"], "Test Comment")
        self.assertEqual(response.json()["email"], "test@example.com")
        self.assertEqual(response.json()["body"], "This is a test comment")

if __name__ == "__main__":
    unittest.main()