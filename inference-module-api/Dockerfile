FROM public.ecr.aws/lambda/python:3.8

# install our dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY handler.py ${LAMBDA_TASK_ROOT}
COPY ./models/* ${LAMBDA_TASK_ROOT}
COPY ./artifacts/* ${LAMBDA_TASK_ROOT}
COPY config.ini ${LAMBDA_TASK_ROOT}
COPY helper.py ${LAMBDA_TASK_ROOT}
COPY stopwords.txt ${LAMBDA_TASK_ROOT}

CMD [ "handler.handler" ]