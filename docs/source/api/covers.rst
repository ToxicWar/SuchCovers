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
        }

    :status 201: Covers loaded
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
