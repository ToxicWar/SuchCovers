Обложки
=======


Добавление обложки
------------------

.. http:post:: /covers/

    .. sourcecode:: http

        POST /covers/ HTTP/1.1
        Content-Type:application/json

        {
        }

    .. sourcecode:: http

        HTTP/1.0 201 CREATED
        Content-Type: application/json

        {
            "title": "Test",
            "tags": "admin, test"
        }

    :status 201: Cover create
    :status 400: Invalid data


Получение обложек
-----------------

.. http:get:: /covers/

    .. sourcecode:: http

        GET /covers/ HTTP/1.1
        Content-Type:application/json

    .. sourcecode:: http

        HTTP/1.0 200 OK
        Content-Type: application/json

        {
            "count": 2,
            "next": null,
            "previous": null,
            "results": [
                {
                    "id": 1,
                    "title": "Title",
                    "image": "/media/covers/KABOOM_Adventure_Time_v3_OGN_2.jpg",
                    "tags": [
                        "test",
                        "lol"
                    ],
                    "likes": 10,
                    "is_display": true
                },
                {
                    "id": 2,
                    "title": "Yay",
                    "image": "/media/covers/6eSxs6p.png",
                    "tags": [
                        "muchtached"
                    ],
                    "likes": 0,
                    "is_display": true
                }
            ]
        }

    :status 201: Covers created
    :status 400: Invalid data


Получение обложки
-----------------

.. http:get:: /covers/{id}

    .. sourcecode:: http

        GET /covers/{id} HTTP/1.1
        Content-Type:application/json

    .. sourcecode:: http

        HTTP/1.0 200 OK
        Content-Type: application/json

        {
            "id": 1,
            "title": "Title",
            "image": "/media/covers/KABOOM_Adventure_Time_v3_OGN_2.jpg",
            "tags": [
                "test",
                "lol"
            ],
            "likes": 10,
            "is_display": true
        }

    :status 201: Cover loaded
    :status 400: Invalid data


Удаление обложки
----------------

.. http:delete:: /covers/{id}

    .. sourcecode:: http

        DELETE /covers/{id} HTTP/1.1
        Content-Type:application/json

    .. sourcecode:: http

        HTTP/1.0 204 No Content

    :status 204: No content
    :status 400: Invalid data
