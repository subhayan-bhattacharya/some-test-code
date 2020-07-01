import sample.resource
import sample.configuration
import dataclasses
import flask
import flask_restful


def main():
    subhayan = sample.resource.Person(name="Subhayan", year=1984)
    resource_cls_kwargs = dataclasses.asdict(
        sample.configuration.ResourceClsKwargs(person=subhayan)
    )
    app = flask.Flask(__name__)
    api = flask_restful.Api(app)
    api.add_resource(
        sample.resource.SampleResource,
        "/sample",
        resource_class_kwargs=resource_cls_kwargs,
    )
    return app


if __name__ == "__main__":
    app = main()
    app.run(debug=True)
