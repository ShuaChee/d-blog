# Description
You need to create a distributed web application which implements a Blog with Posts and Comments. This application comprises two Django projects:
- `blog_backend` (backend), which should implement the REST API and contain the major business logic
- `blog` (frontend), which should represent the user interface and use the `blog_backend` API for data manipulation
You will have to implement the REST API and communication mechanism between two projects. Please, see some details below.



# Project structure and details
- Use the provided project structure template as a backbone (in both Backend and Frontend parts)
- Use the version control system (either Git or Mercurial)
- Create a new virtualenv for both projects.
- The dependencies are in the requirements.txt for each project.
- The `blog_backend` should implement the API and run on port 8002 (or you can customize the port number in blog/settings.py:BACKEND_API_URL).
- The `blog` (frontend) should use this API and can run on any port you want.
- There is a data migration that creates 3 example blog posts and there are schema migrations that create your database.
- All business logic should be placed in services. An extremely simple example of that can be seen in blog_backend/bb_post/services/post.py



# The assignments
- Add users to the blog (users can create an account, they should have a username, email address and password)
- Users should verify their email address via a token that is sent by email, upon clicking on the token the user should be verified
- Add comments to the blog (only logged-in users can place comments, everyone can see them though)
- Add a migration that will create some test comments in DB (should be reversable)
- Cover services and API with unit tests (hint: use `mock` library) (a big plus)
- Extra: Add gravatar pictures for users that are displayed for each comment under a blog post (nice to have but not required)








