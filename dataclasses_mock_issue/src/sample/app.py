import sample.resource
import sample.configuration
import dataclasses
import flask
import flask_restful


def main(person):
    # resource_cls_kwargs = dataclasses.asdict(
    #     sample.configuration.ResourceClsKwargs(person=person)
    # )
    # resource_cls_kwargs = sample.configuration.ResourceClsKwargs(person=person)._asdict()
    resource_cls_kwargs = sample.configuration.ResourceClsKwargs(person=person).asdict()
    app = flask.Flask(__name__)
    api = flask_restful.Api(app)
    api.add_resource(
        sample.resource.SampleResource,
        "/sample",
        resource_class_kwargs=resource_cls_kwargs,
    )
    return app


if __name__ == "__main__":
    subhayan = sample.resource.Person(name="Subhayan", year=1984)
    app = main(subhayan)
    app.run(debug=True)
