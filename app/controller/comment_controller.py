from typing import List # 전체 조회 (read)
from bson import ObjectId # objectid = comment id
from fastapi import APIRouter # router (crud)
from app.service.comment_service import CommentService # comment service
from app.model.comment import Comment, CommentUpdate # comment model
from app.model.reply import Reply # reply model

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
async def update_comment(comment_id: str, comment: CommentUpdate): # comment id로 comment 일부 수정
     comment_update = await service.update_service(ObjectId(comment_id), comment.model_dump())
     return await comment_update

# 3. 삭제 (delete)
@router.delete("/comment/{comment_id}") 
async def delete_comment(comment_id: str): # comment id로 comment 삭제
    comment_delete = service.delete_service(ObjectId(comment_id)) 
                            # objectid = comment id
    return await comment_delete 

# 6. 대댓글 추가 (create) 
@router.post("/comment/{comment_id}/reply", response_model=Comment) # comment에 reply 추가
async def create_comment_from_reply(comment_id: str, reply: Reply): 
            # commentid : 입력 값 => str, reply : reply collection에 data를 추가로 Reply model 사용
    new_reply =  await service.create_service_from_reply(ObjectId(comment_id), reply.model_dump()) 
                                # 생성한 reply의 data 값을 comment에 추가한 값을 반환 
    # reply.model_dump : data 생성 후 json 형태로 저장 
    return await new_reply # 생성한 reply의 data를 결과값으로 반환함