"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Friends(Controller):
    def __init__(self, action):
        super(Friends, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('Friend')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        friends = self.models['Friend'].get_all()
        return self.load_view('index.html', friends=friends)

    def add(self):
        return self.load_view('add.html')

    def show_one(self, id):
        one_friend = self.models['Friend'].get_one_friend(id)
        # print one_friend
        return self.load_view('show.html', one_friend=one_friend)

    def update(self, id):
        one_friend = self.models['Friend'].get_one_friend(id)
        return self.load_view('update.html', one_friend=one_friend)

    def delete(self, id):
        self.models['Friend'].delete_friend(id)
        return redirect('/')

    # Post methods
    def add_process (self):
        details = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'occupation': request.form['occupation'],
            'known_for': request.form['known_for'],
        }
        self.models['Friend'].add_friend(details)
        return redirect('/')

    def update_process(self, id):
        # details = {
        #     'id': id,
        #     'first_name': request.form['first_name'],
        #     'last_name': request.form['last_name'],
        #     'occupation': request.form['occupation'],
        #     'known_for': request.form['known_for']
        # }
        self.models['Friend'].update_friend(request.form, id)
        return redirect('/')

