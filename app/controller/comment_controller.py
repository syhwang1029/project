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
# 4. 조회 (read)
@router.get("/comment/",  response_model=list[Comment])# response_model : 응답 처리 model
                            # list로 전체 comment 조회
async def read_comment():
    return await service.read_service()

# 5. 일부 조회 (read)
@router.get("/comment/{comment_id}", response_model=Comment)
async def read_comment_comentid(comment_id: str):
    return await service.read_service_commentid(comment_id)


# 1. 생성 (create)
@router.post("/comment/", response_model=Comment)
async def create_comment(comment: Comment):
    return await service.create_service(comment)
    
# 2. 수정 (update)
@router.put("/comment/{comment_id}", response_model=Comment)
async def update_comment(comment_id: str, comment: CommentUpdate):
    return await service.update_service(comment_id, comment)

# 3. 삭제 (delete)
@router.delete("/comment/{comment_id}", response_model=str)
async def delete_comment(comment_id: str):
    return await service.delete_service(comment_id)