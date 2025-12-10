import logging

from docling.models.base_model import BasePageModel
from docling.models.factories.base_factory import BaseFactory

logger = logging.getLogger(__name__)


class TableStructureFactory(BaseFactory[BasePageModel]):
    def __init__(self, *args, **kwargs):
        super().__init__("table_structure_engines", *args, **kwargs)
