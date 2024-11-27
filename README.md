# Sh33p Blog

A Flask based backend for creating your own blog.

## Instructions

- Clone the repository on your server \
`>` `git clone https://github.com/Yurand2000/sh33p-blog`

- Configure your blog (see the **Configuration** section)

- *cd* into the cloned repository \
`>` `cd sh33p-blog`

- Build your containerized application \
`>` `docker compose build`

- Run your application \
`>` `docker compose up`

## Configuration

*Work in progress*

## Development

If you want to update the application code or pages and see their changes live, you can switch to the *dev* configuration. Keep in mind that the application must not be deployed on your server in this configuration for security reasons.

- Clone sh33p-blog on your local machine \
`>` `git clone https://github.com/Yurand2000/sh33p-blog`

- *cd* into the cloned repository \
`>` `cd sh33p-blog`

- Setup your *dev* environment
    - Create the following directory tree
        ```
        sh33p-blog/
          | local/
          |    data/
          |    static/
          | ...
        ```
    - Create the symbolic link *local/app -> ../flask/app* \
    `>` `ls -s ../flask/app local/app`
    - *(OPTIONAL)* Copy the default files as a template for your blog \
        Copy `file-server/static/*` in `local/static` \
        Copy `flask/data` in `local/data`

- Build and start the application in *dev* mode \
`>` `docker compose -f compose_dev.yaml build` \
`>` `docker compose -f compose_dev.yaml up`

The application will now fetch the code from your `local/app` directory, static data from `local/static` and pages data from `local/data`.

## License

The source code is licensed under [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/). If you do not alter the source code in any way, but just add/remove pages and static files, you can freely use this software for your own blogs.