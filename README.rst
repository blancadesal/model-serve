Overview
========

This is some starter code for a Flask-Celery-Redis app with WebSocket support through `eventlet`.
It contains a few tasks that can be used to manually test out the functionality.
Right now, Redis is used as both the message broker and the results backend, but a production app for CV model serving would rather use RabbitMQ as the message broker.


Quick start
-----------

You need to have docker and docker-compose installed.
Clone the repo and cd into the root directory, then:

.. code-block:: bash

   $ docker-compose up -d --build

Get the logs in another terminal tab:

.. code-block:: bash

   $ docker-compose logs -f


* Navigate to http://localhost:5557/dashboard for Flower (Celery monitoring tool)
* Navigate to http://localhost:5010/users/form/ to simulate a long-running background task, using WebSockets to push the result to the client.
