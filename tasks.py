#!/usr/bin/env python

"""
Deployment file to facilitate releases of monty.
"""

from __future__ import division

import glob
import requests
import json
import os
import re
import subprocess
from pathlib import Path
from invoke import task
from monty.os import cd


@task
def cleanup(ctx):
    with cd("lectures/slides_tex"):
        ctx.run("rm *.toc *.snm *.aux *.vrb *.log *.nav *.out *.bbl *.blg", warn=True)
        ctx.run("rm -r _minted*", warn=True)


@task
def build_pdf(ctx, fname):
    with cd("lectures/slides_tex"):
        fn = fname.rstrip(".tex")
        ctx.run('pdflatex -shell-escape "%s"' % fn)
        ctx.run('bibtex "%s"' % fn, warn=True)
        ctx.run('pdflatex -shell-escape "%s"' % fn)
        ctx.run('pdflatex -shell-escape "%s"' % fn)
        ctx.run("mv *.pdf ../slides", warn=True)


@task
def build_all(ctx):
    status = subprocess.check_output(["git", "diff", "--name-only", "HEAD"])
    changed = [Path(l).name for l in status.decode("utf").split("\n") if l.endswith(".tex")]
    if changed:
        for fname in changed:
            build_pdf(ctx, fname)
        cleanup(ctx)
