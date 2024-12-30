from typing import List
from bson import ObjectId
from fastapi import APIRouter # router
from app.service.comment_service import CommentService # comment service
from app.model.comment import Comment, CommentUpdate # comment model

# comment router (crud)
router = APIRouter(
    prefix="/comments", 
    tags=["comment"]
)

service =  CommentService() # comment service


## 댓글 (comment) ##
# 1. 생성 (create)
@router.post("/comment/", response_model=Comment) # response_model : 응답 처리 model
async def create_comment(comment: Comment):
    new_comment = await service.create_service(comment.model_dump()) # model_dump : json 형태로 변환
    return await new_comment

# 4. 전체 조회 (read)
@router.get("/comment/", response_model=List[Comment]) # list 형태로 comment 전체 조회
async def read_comment():
    return await service.read_service()

# 5. 일부 조회 (read) - comment id 
@router.get("/comment/{comment_id}", response_model=Comment) # 경로 매개변수 순서대로 지정함
async def raed_comment_commentid(comment_id: str): # comment id로 comment 일부 조회
    comment = service.read_service_commentid(ObjectId(comment_id)) # comment_id = ObjectId
    return await comment
    
# 2. 수정 (update)
@router.put("/comment/{comment_id}", response_model=Comment)
async def update_comment(comment_id: str, comment: CommentUpdate):
     comment_update = await service.update_service(ObjectId(comment_id), comment.model_dump())
     return await comment_update

# 3. 삭제 (delete)
@router.delete("/comment/{comment_id}", response_model=str) # comment id : str
async def delete_comment(comment_id: str):
    comment_delete = service.delete_service(ObjectId(comment_id))
    return await comment_delete