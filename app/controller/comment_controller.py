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
@router.post("/comment/", response_model=Comment)
async def create_comment(comment: Comment):
    new_comment = await service.create_service(comment.model_dump()) # model_dump : json 형태로 변환
    return await new_comment

# 4. 전체 조회 (read)
@router.get("/comment/", response_model=List[Comment]) # list 형태로 comment 전체 조회
async def read_comment():
    return await service.read_service()

# 5. 일부 조회 (read) - comment id
@router.get("/comment/{comment_id}", response_model=Comment)# response_model : 응답 처리 model
                            # list로 전체 comment 조회
async def raed_comment_commentid(comment_id: str):
    comment = await service.read_service_commentid(ObjectId(comment_id))
    return await comment
    
# 2. 수정 (update)
@router.put("/comment/{comment_id}", response_model=Comment)
async def update_comment(comment_id: str, comment: CommentUpdate):
    return await service.update_service(comment_id, comment)

# 3. 삭제 (delete)
@router.delete("/comment/{comment_id}", response_model=str)
async def delete_comment(comment_id: str):
    comment_delete = await service.delete_service(ObjectId(comment_id))
    return await comment_delete