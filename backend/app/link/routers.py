from fastapi import APIRouter, Body, HTTPException, Path, Request, status

from fastapi.responses import RedirectResponse, JSONResponse

from . import database
from .models import Link
from .schemas import UrlIn
from .utils import calculate_url_key

router = APIRouter()


@router.on_event("startup")
async def startup():
    await database.startup()


@router.on_event("shutdown")
async def shutdown():
    await database.shutdown()


@router.put('/link', status_code=status.HTTP_201_CREATED)
async def create_short_link(request: Request, item: UrlIn = Body(...)):
    slug = calculate_url_key(item.url) if item.slug is None else item.slug
    host_path = str(request.url)[:-4:]
    await Link.create(url=item.url, slug=slug)
    return {'link': f'{host_path}{slug}'}



@router.get('/{slug}')
async def redirect_short_link(slug: str = Path(..., min_length=5)):
    item = await Link.get_or_none(slug=slug)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'Short link does not exist'})
    return RedirectResponse(item.url)


