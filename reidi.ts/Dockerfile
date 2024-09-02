FROM oven/bun:latest


WORKDIR /app

COPY ./src ./src
COPY ./package.json ./
COPY ./sqlite.db ./
COPY ./tsconfig.json ./ 
    
RUN bun install

CMD ["bun", "run", "src/index.ts"]
