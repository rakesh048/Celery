                        ######## Celery ########
   
   Celery is an asynchronous task queue/job queue based on distributed message passing. 
   It is focused on real-time operation, but supports scheduling as well.
   
   # Dependency

            Install django (redme repository from Login-authentication-with-Django-Angularjs-AngularMaterial)
            pip install celery (3.1.25)
            pip install django-celery (3.1.17)
            apt-get update
            sudo apt-get install rabbitmq-server (broker which i am using)
            cd celery_task
            *** run the worker ***
            celery -A celery_task worker -B --loglevel=info
            *** run the celery beat ***
            celery -A celery_task beat

            Now you can see in celery_task there is created log file name celerylogfile.log
            you can run it on terminal by tailf celerylogfile.log.
        
  ThankYou,

