""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Friend(Model):
    def __init__(self):
        super(Friend, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database
    """
    def get_all(self):
        query = "SELECT * from friends"
        return self.db.query_db(query)

    def get_one_friend(self, id):
        query = "SELECT * from friends where id = :id"
        data = {'id': id}
        result = self.db.query_db(query, data)
        print result
        return result[0]

    def add_friend(self, friend):
        sql = "INSERT into friends (first_name, last_name, occupation, known_for, created_at, updated_at) values(:first_name, :last_name, :occupation, :known_for, NOW(), NOW())"
        data = {'first_name': friend['first_name'],
                'last_name':friend['last_name'],
                'occupation': friend['occupation'],
                'known_for': friend['known_for']
                }
        return self.db.query_db(sql, data)

    
    def update_friend(self, friend, id):
        query = "UPDATE friends SET first_name=:first_name, last_name =:last_name, occupation=:occupation, known_for=:known_for WHERE id = :id"
        data = {'first_name': friend['first_name'],
                'last_name':friend['last_name'],
                'occupation': friend['occupation'],
                'known_for': friend['known_for'],
                'id': id}
        return self.db.query_db(query, data)

    def delete_friend(self, id):
        query = "DELETE FROM friends WHERE id = :id"
        data = {"id": id}
        return self.db.query_db(query, data)

