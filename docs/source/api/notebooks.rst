Тетрадки
========


Добавление тетради
------------------

.. http:post:: /notebooks/

    .. sourcecode:: http

        POST /notebooks/ HTTP/1.1
        Content-Type:application/json

        {
            "cover": {"title": "Yay"},
            "pages": 20
        }

        или

        {
            "cover": 2,
            "pages": 20
        }

    .. sourcecode:: http

        HTTP/1.0 201 CREATED
        Content-Type: application/json

        {
        }

    :status 201: Notebook created
    :status 400: Invalid data


Получение тетрадей
------------------

.. http:get:: /notebooks/

    .. sourcecode:: http

        GET /notebooks/ HTTP/1.1
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
                    "cover": {
                        "id": 2,
                        "title": "Yay",
                        "image": "/media/covers/6eSxs6p.png",
                        "tags": [
                            "muchtached"
                        ],
                        "likes": 0,
                        "is_display": true
                    },
                    "pages": 20
                },
                {
                    "id": 2,
                    "cover": {
                        "id": 9,
                        "title": "Duck",
                        "image": "/media/covers/IMG_21102012_203424.png",
                        "tags": [
                            "duck"
                        ],
                        "likes": 0,
                        "is_display": true
                    },
                    "pages": 12
                }
            ]
        }

    :status 200: Notebooks loaded
    :status 400: Invalid data


Получение тетради
-----------------

.. http:get:: /notebooks/{id}

    .. sourcecode:: http

        GET /notebooks/{id} HTTP/1.1
        Content-Type:application/json

    .. sourcecode:: http

        HTTP/1.0 200 OK
        Content-Type: application/json

        {
            "id": 1,
            "cover": {
                "id": 2,
                "title": "Yay",
                "image": "/media/covers/6eSxs6p.png",
                "tags": [
                    "muchtached"
                ],
                "likes": 0,
                "is_display": true
            },
            "pages": 20
        }

    :status 200: Ok
    :status 400: Invalid data


Обновление тетради
------------------

.. http:put:: /notebooks/{id}

    .. sourcecode:: http

        PUT /notebooks/{id} HTTP/1.1
        Content-Type:application/json

    .. sourcecode:: http

        HTTP/1.0 200 OK
        Content-Type: application/json

        {
        }

    :status 200: Notebook updated
    :status 400: Invalid data


Удаление тетради
----------------

.. http:delete:: /notebooks/{id}

    .. sourcecode:: http

        DELETE /notebooks/{id} HTTP/1.1
        Content-Type:application/json

    .. sourcecode:: http

        HTTP/1.0 204 No Content

    :status 204: No content
    :status 400: Invalid data
