from concurrent import futures
from flags import get_flag,show,save_flag,main
def download_one(cc):
    image=get_flag(cc)
    show(cc)
    save_flag(image,cc.lower()+'.gif')
    return cc

def download_many(cc_list):
    #ProcessPoolExecutor类不需设置max_workers参数，默认使用电脑cpu的数量
    with futures.ProcessPoolExecutor() as executor:
        res=executor.map(download_one,sorted(cc_list))#download_one函数会在多个线程中并发调用；map方法返回一个生成器
    return len(list(res))

if __name__ == '__main__':
    main(download_many)