from __future__ import annotations

from typing import cast

import qik.conf
import qik.func
import qik.unset


class PygraphDepConf(qik.conf.Dep, tag="pygraph", frozen=True):
    pyimport: str


class PygraphPluginConf(qik.conf.Base, frozen=True, dict=True):
    ignore_type_checking: bool = False
    ignore_pydists: bool = False
    ignore_missing_module_pydists: bool = False
    module_pydists: dict[str, str] = {}
    cache: str | qik.unset.UnsetType = qik.unset.UNSET
    build_cache: str | qik.unset.UnsetType = qik.unset.UNSET
    lock_cache: str | qik.unset.UnsetType = qik.unset.UNSET

    @qik.func.cached_property
    def resolved_build_cache(self) -> str:
        return cast(
            str,
            qik.unset.coalesce(
                self.build_cache, self.cache, qik.conf.project().plugin_cache, default="repo"
            ),
        )

    @qik.func.cached_property
    def resolved_lock_cache(self) -> str:
        return cast(
            str,
            qik.unset.coalesce(
                self.lock_cache, self.cache, qik.conf.project().plugin_cache, default="repo"
            ),
        )


qik.conf.register_type(PygraphDepConf, "qik.pygraph.dep.factory")
qik.conf.register_conf(PygraphPluginConf, "qik.pygraph")
