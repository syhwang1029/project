from bson import ObjectId
from app.service.reply_service import ReplyService # reply service
from app.model.reply import Reply# reply model
from fastapi import APIRouter # FastAPI router

# reply router (crud)
router = APIRouter( 
# router = FastAPI()
    prefix="/replys", # url 접두사
    tags=["reply"]
)

# reply controller
service = ReplyService() # reply service


## 대댓글 (reply) ##
# 1. 생성 (create) 
@router.post("/reply/", response_model=Reply) 
    # response_model : Reply model로 cilent에게 응답 처리
async def create_reply(reply: Reply): # data 입력 형식 model : Reply
    return await service.crate_service(reply.model_dump()) # model_dump : 파이썬 객체를 json 형태로 직렬화

# 4. 전체 조회 (read)
# 경로 매개변수 순서대로 지정함 : "/reply/" -> "/reply/{relpy_id}"

# 5. 일부 조회 (read) - replyid
@router.get("/reply/{reply_id}", response_model=Reply) # replyid로 일부 reply의 data 조회
async def read_reply_replyid(reply_id: str): # reply id 입력받음
    replys = service.read_service_replyid(ObjectId(reply_id)) # objectid = reply id
    return await replys
    
    

    
    
# 2. 수정 (update)
    
# 3. 삭제 (delete)