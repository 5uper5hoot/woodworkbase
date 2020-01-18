from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.ext.declarative import declarative_base, declared_attr

if TYPE_CHECKING:
    from typing import Dict, Any


class _Base:

    # see: https://github.com/topsport-com-au/topsport/issues/191
    # ensures that this type isn't inferred as Dict[str, str] as
    # happens when the `"polymorphic_on"` key is always defined
    # first on root class of polymorphic heirarchies.
    __mapper_args__: Dict[str, Any]

    @declared_attr
    def __table__(cls):
        return cls.__name__.lower()

    def __repr__(self) -> str:
        fmt = "{}.{}({})"
        package = self.__class__.__module__
        class_ = self.__class__.__name__
        attrs = sorted(
            (col.name, getattr(self, col.name)) for col in self.__table__.columns
        )
        sattrs = ", ".join("{}={!r}".format(*x) for x in attrs)
        return fmt.format(package, class_, sattrs)


Base = declarative_base(cls=_Base)
