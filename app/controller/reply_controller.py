from typing import List
from bson import ObjectId
from app.service.reply_service import ReplyService # reply service
from app.model.reply import Reply, ReplyUpdate # reply model
from fastapi import APIRouter # FastAPI router

# reply router (crud)
router = APIRouter( 
# router = FastAPI()
    prefix="/replys", # url 접두사
    tags=["reply"]
)

service = ReplyService() # reply service


## 대댓글 (reply) ##
# 1. 생성 (create) 
@router.post("/reply/", response_model=Reply) 
    # response_model : Reply model로 cilent에게 응답 처리
async def create_reply(reply: Reply): # data 입력 형식 model : Reply
    new_reply = await service.crate_service(reply.model_dump()) # model_dump : python 객체를 json 형태로 직렬화
    return await new_reply

# 4. 전체 조회 (read)
@router.get("/reply/", response_model=List[Reply]) # list 형태로 전체 reply 조회
async def read_reply():
    return await service.read_service() 


# 5. 일부 조회 (read) - replyid
""" 경로 매개변수 순서대로 지정함 
 : @router.get("/reply/") 
 => @router.get("/reply/{relpy_id}") """
@router.get("/reply/{reply_id}", response_model=Reply) # replyid로 일부 reply의 data 조회
async def read_reply_replyid(reply_id: str): # replyid를 입력 받기 때문에 str으로 지정함
    replys = service.read_service_replyid(ObjectId(reply_id)) # objectid = reply id
    return await replys # replyid로 지정한 reply의 data 조회 결과값 반환함
    
    
# 2. 수정 (update)
# put : 전체 수정
# patch : 일부 수정
@router.put("/reply/{reply_id}", response_model=Reply) # replyid로 reply의 data 수정
async def update_reply(reply_id: str, reply: ReplyUpdate): # relpy id로 지정 후 reply의 data 수정 
    reply_update = await service.update_service(ObjectId(reply_id), reply.model_dump()) 
                    # objectid = replyid, reply : data
                    # model_dump : python 객체를 json 형태로 직렬화함
    return await reply_update # json 형태로 수정한 reply의 data 결과값 반홤함

# 3. 삭제 (delete)
@router.delete("/relpy/{reply_id}") # relpyid로 reply 삭제
async def delete_reply(reply_id: str): # replyid를 입력 받아 지정하기 때문에 str으로 지정함
    reply_delete = service.delete_service(ObjectId(reply_id)) # objectid = reply id
    return await reply_delete # 지정한 objectid로 reply 삭제 후 결과값 반환함